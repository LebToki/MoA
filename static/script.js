// Modern JavaScript for MoA Chatbot
(function() {
  'use strict';

  // Theme Management
  class ThemeManager {
    constructor() {
      this.theme = this.getStoredTheme() || this.getSystemTheme();
      this.init();
    }

    getSystemTheme() {
      return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }

    getStoredTheme() {
      return localStorage.getItem('theme');
    }

    setTheme(theme) {
      this.theme = theme;
      document.documentElement.setAttribute('data-theme', theme);
      localStorage.setItem('theme', theme);
      this.updateToggleButton();
    }

    toggleTheme() {
      const newTheme = this.theme === 'dark' ? 'light' : 'dark';
      this.setTheme(newTheme);
    }

    updateToggleButton() {
      const checkbox = document.getElementById('theme-toggle');
      if (checkbox) {
        // Checkbox checked = dark mode, unchecked = light mode
        checkbox.checked = this.theme === 'dark';
      }
    }

    init() {
      // Set initial theme
      this.setTheme(this.theme);

      // Listen for system theme changes
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!this.getStoredTheme()) {
          this.setTheme(e.matches ? 'dark' : 'light');
        }
      });

      // Setup toggle switch
      const toggleSwitch = document.getElementById('theme-toggle');
      if (toggleSwitch) {
        toggleSwitch.addEventListener('change', () => this.toggleTheme());
      }
    }
  }

  // Chat Utilities
  class ChatUtils {
    static scrollToBottom(element) {
      if (element) {
        element.scrollTop = element.scrollHeight;
      }
    }

    static formatMessage(content) {
      // Enhanced markdown-like formatting
      let formatted = content
        // Code blocks (triple backticks)
        .replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>')
        // Inline code (single backticks)
        .replace(/`([^`]+)`/g, '<code>$1</code>')
        // Bold text
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        // Italic text
        .replace(/\*(.*?)\*/g, '<em>$1</em>')
        // Line breaks
        .replace(/\n/g, '<br>');
      
      return formatted;
    }

    static showLoading(element) {
      if (element) {
        element.innerHTML = `
          <div class="loading">
            <span>Thinking</span>
            <div class="loading-dots">
              <span class="loading-dot"></span>
              <span class="loading-dot"></span>
              <span class="loading-dot"></span>
            </div>
          </div>
        `;
      }
    }
  }

  // Form Enhancement
  class FormEnhancer {
    constructor() {
      this.init();
    }

    init() {
        // Auto-resize textarea (chat input)
      const textarea = document.getElementById('instruction');
      const chatInput = document.querySelector('.chat-input');
      const inputElement = textarea || chatInput;
      
      if (inputElement) {
        inputElement.addEventListener('input', function() {
          this.style.height = 'auto';
          this.style.height = Math.min(this.scrollHeight, 200) + 'px';
        });

        // Handle Enter key (Ctrl+Enter to submit, Shift+Enter for new line)
        inputElement.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' && e.ctrlKey) {
            e.preventDefault();
            const form = inputElement.closest('form');
            if (form) {
              form.submit();
            }
          }
        });
      }

      // File input enhancement
      const fileInput = document.getElementById('file');
      if (fileInput) {
        fileInput.addEventListener('change', function(e) {
          const fileName = e.target.files[0]?.name;
          if (fileName) {
            const label = this.previousElementSibling;
            if (label && label.tagName === 'LABEL') {
              const originalText = label.textContent;
              label.textContent = `File: ${fileName}`;
              setTimeout(() => {
                label.textContent = originalText;
              }, 3000);
            }
          }
        });
      }

      // Form submission enhancement
      const forms = document.querySelectorAll('form');
      forms.forEach(form => {
        form.addEventListener('submit', function(e) {
          const submitBtn = this.querySelector('button[type="submit"]');
          if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span class="btn-icon">⏳</span> Processing...';
            
            // Re-enable after 5 seconds as fallback
            setTimeout(() => {
              submitBtn.disabled = false;
              submitBtn.innerHTML = 'Submit';
            }, 5000);
          }
        });
      });
    }
  }

  // Conversation List Enhancement
  class ConversationList {
    constructor() {
      this.init();
    }

    init() {
      // Highlight active conversation
      const currentPath = window.location.pathname;
      const links = document.querySelectorAll('.conversation-link');
      
      links.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
          link.classList.add('active');
        }
      });

      // Add click handlers for better UX
      links.forEach(link => {
        link.addEventListener('click', function(e) {
          // Add loading state
          links.forEach(l => l.classList.remove('active'));
          this.classList.add('active');
        });
      });
    }
  }

    // Flash Message Handler
    class FlashMessageHandler {
        constructor() {
            this.init();
        }

        init() {
            const flashMessages = document.querySelectorAll('.flash-message');
            flashMessages.forEach(msg => {
                // Auto-dismiss after 5 seconds
                setTimeout(() => {
                    msg.style.transition = 'opacity 0.3s ease-out';
                    msg.style.opacity = '0';
                    setTimeout(() => msg.remove(), 300);
                }, 5000);

                // Click to dismiss
                msg.addEventListener('click', function() {
                    this.style.transition = 'opacity 0.3s ease-out';
                    this.style.opacity = '0';
                    setTimeout(() => this.remove(), 300);
                });
            });
        }
    }

    // Initialize everything when DOM is ready
    document.addEventListener('DOMContentLoaded', function() {
        // Set current year in footer
        const yearElement = document.getElementById('current-year');
        if (yearElement) {
            yearElement.textContent = new Date().getFullYear();
        }
        
        // Initialize theme manager
        new ThemeManager();

        // Initialize form enhancements
        new FormEnhancer();

        // Initialize conversation list
        new ConversationList();

        // Initialize flash messages
        new FlashMessageHandler();

    // Auto-scroll chat to bottom
    const chatBox = document.querySelector('.chat-box');
    if (chatBox) {
      ChatUtils.scrollToBottom(chatBox);
      
      // Scroll to bottom when new messages are added (for future streaming)
      const observer = new MutationObserver(() => {
        ChatUtils.scrollToBottom(chatBox);
      });
      
      observer.observe(chatBox, {
        childList: true,
        subtree: true
      });
    }

    // Add smooth transitions
    document.body.style.opacity = '0';
    setTimeout(() => {
      document.body.style.transition = 'opacity 0.3s ease-in';
      document.body.style.opacity = '1';
    }, 10);
  });

  // Handle page visibility for better UX
  document.addEventListener('visibilitychange', function() {
    if (!document.hidden) {
      const chatBox = document.querySelector('.chat-box');
      if (chatBox) {
        ChatUtils.scrollToBottom(chatBox);
      }
    }
  });

})();
