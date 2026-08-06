document.addEventListener('DOMContentLoaded', () => {
  // --- Header Scroll Effect ---
  const header = document.querySelector('header');
  const handleScroll = () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };
  window.addEventListener('scroll', handleScroll);
  handleScroll(); // Run once on load to catch already scrolled states

  // --- Mobile Navigation Menu Toggle ---
  const navToggle = document.querySelector('.nav-toggle');
  const navMenu = document.querySelector('.nav-menu');
  const navLinks = document.querySelectorAll('.nav-link');

  if (navToggle && navMenu) {
    navToggle.addEventListener('click', () => {
      navMenu.classList.toggle('active');
      
      // Animate hamburger toggle to X
      const spans = navToggle.querySelectorAll('span');
      if (navMenu.classList.contains('active')) {
        spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
        spans[1].style.opacity = '0';
        spans[2].style.transform = 'rotate(-45deg) translate(7px, -7px)';
      } else {
        spans[0].style.transform = 'none';
        spans[1].style.opacity = '1';
        spans[2].style.transform = 'none';
      }
    });

    // Close menu when clicking a link
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        const spans = navToggle.querySelectorAll('span');
        spans[0].style.transform = 'none';
        spans[1].style.opacity = '1';
        spans[2].style.transform = 'none';
      });
    });
  }

  // --- Portfolio Category Filtering ---
  const filterButtons = document.querySelectorAll('.filter-btn');
  const portfolioItems = document.querySelectorAll('.portfolio-item');

  if (filterButtons.length > 0 && portfolioItems.length > 0) {
    filterButtons.forEach(button => {
      button.addEventListener('click', () => {
        // Toggle active button state
        filterButtons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');

        const filterValue = button.getAttribute('data-filter');

        portfolioItems.forEach(item => {
          // Add fade transition
          item.style.opacity = '0';
          item.style.transform = 'scale(0.8)';
          
          setTimeout(() => {
            if (filterValue === 'all' || item.getAttribute('data-category') === filterValue) {
              item.style.display = 'block';
              setTimeout(() => {
                item.style.opacity = '1';
                item.style.transform = 'scale(1)';
              }, 50);
            } else {
              item.style.display = 'none';
            }
          }, 300);
        });
      });
    });
  }

  // --- FAQ Accordion Toggle ---
  const faqQuestions = document.querySelectorAll('.faq-question');

  if (faqQuestions.length > 0) {
    faqQuestions.forEach(question => {
      question.addEventListener('click', () => {
        const item = question.parentElement;
        const answer = question.nextElementSibling;
        
        // Toggle active status
        item.classList.toggle('active');

        if (item.classList.contains('active')) {
          answer.style.maxHeight = answer.scrollHeight + 'px';
          answer.style.paddingBottom = '24px';
        } else {
          answer.style.maxHeight = '0';
          answer.style.paddingBottom = '0';
        }

        // Close other items (optional but nice)
        const allItems = document.querySelectorAll('.faq-item');
        allItems.forEach(otherItem => {
          if (otherItem !== item) {
            otherItem.classList.remove('active');
            const otherAnswer = otherItem.querySelector('.faq-answer');
            otherAnswer.style.maxHeight = '0';
            otherAnswer.style.paddingBottom = '0';
          }
        });
      });
    });
  }

  // --- Contact Form Submission Handler ---
  const contactForm = document.getElementById('contact-form');
  const formSuccess = document.querySelector('.form-success-message');

  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      // Collect data (for CRM simulation or console debug)
      const formData = new FormData(contactForm);
      const data = {
        name: formData.get('name'),
        phone: formData.get('phone'),
        email: formData.get('email'),
        service: formData.get('service'),
        message: formData.get('message')
      };

      console.log('Form submission received:', data);

      // Save to local storage as backup lead capture
      let leads = JSON.parse(localStorage.getItem('jds_leads') || '[]');
      leads.push({ ...data, date: new Date().toISOString() });
      localStorage.setItem('jds_leads', JSON.stringify(leads));

      // Visual feedback - Show success overlay and reset form
      formSuccess.style.display = 'block';
      contactForm.style.display = 'none';
      formSuccess.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

      // In production, we'd post to Web3Forms/Formspree/Zapier:
      /*
      fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({
          access_key: "YOUR_ACCESS_KEY_HERE",
          name: data.name,
          email: data.email,
          phone: data.phone,
          subject: `New Lead: ${data.service} from ${data.name}`,
          message: data.message
        })
      });
      */
    });
  }

  // --- Scroll to Top Button Logic ---
  let scrollTopBtn = document.getElementById('custom-scroll-top');
  if (!scrollTopBtn) {
    scrollTopBtn = document.createElement('button');
    scrollTopBtn.id = 'custom-scroll-top';
    scrollTopBtn.className = 'custom-scroll-top';
    scrollTopBtn.setAttribute('aria-label', 'Scroll to top');
    scrollTopBtn.innerHTML = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" style="width:22px;height:22px;min-width:22px;min-height:22px;display:block;margin:0 auto;padding:0;"><polyline points="18 15 12 9 6 15"></polyline></svg>';
    document.body.appendChild(scrollTopBtn);
  }

  const toggleScrollTopBtn = () => {
    if (window.scrollY > 300) {
      scrollTopBtn.classList.add('visible');
    } else {
      scrollTopBtn.classList.remove('visible');
    }
  };

  window.addEventListener('scroll', toggleScrollTopBtn);
  toggleScrollTopBtn();

  scrollTopBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  // --- Before & After Interactive Slider & Animation Handler ---
  const baContainer = document.getElementById('ba-slider');
  const baBeforeWrapper = document.getElementById('ba-before-wrapper');
  const baBeforeImg = document.getElementById('ba-before-img');
  const baAfterImg = document.getElementById('ba-after-img');
  const baHandle = document.getElementById('ba-handle');
  const baTabs = document.querySelectorAll('.ba-tab-btn');
  const baProjectTitle = document.getElementById('ba-project-title');
  const baProjectDesc = document.getElementById('ba-project-desc');
  const baAutoScanBtn = document.getElementById('ba-autoscan-btn');

  if (baContainer && baBeforeWrapper && baHandle) {
    let isDragging = false;
    let isScanning = false;
    let scanDirection = 1;
    let scanPos = 50;
    let scanInterval = null;

    const setSliderPos = (percentage) => {
      percentage = Math.max(0, Math.min(100, percentage));
      baBeforeWrapper.style.width = `${percentage}%`;
      baHandle.style.left = `${percentage}%`;
    };

    const updateImageDimensions = () => {
      if (baContainer && baBeforeImg) {
        baBeforeImg.style.width = `${baContainer.offsetWidth}px`;
      }
    };

    window.addEventListener('resize', updateImageDimensions);
    updateImageDimensions();

    const handleMove = (clientX) => {
      const rect = baContainer.getBoundingClientRect();
      const x = clientX - rect.left;
      const percentage = (x / rect.width) * 100;
      setSliderPos(percentage);
    };

    // Mouse Events
    baContainer.addEventListener('mousedown', (e) => {
      isDragging = true;
      stopAutoScan();
      handleMove(e.clientX);
    });

    window.addEventListener('mousemove', (e) => {
      if (isDragging) handleMove(e.clientX);
    });

    window.addEventListener('mouseup', () => {
      isDragging = false;
    });

    // Touch Events for Mobile
    baContainer.addEventListener('touchstart', (e) => {
      isDragging = true;
      stopAutoScan();
      if (e.touches.length > 0) handleMove(e.touches[0].clientX);
    }, { passive: true });

    window.addEventListener('touchmove', (e) => {
      if (isDragging && e.touches.length > 0) handleMove(e.touches[0].clientX);
    }, { passive: true });

    window.addEventListener('touchend', () => {
      isDragging = false;
    });

    // Preset Tabs Switcher
    baTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        baTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');

        const beforeSrc = tab.getAttribute('data-before');
        const afterSrc = tab.getAttribute('data-after');
        const title = tab.getAttribute('data-title');
        const desc = tab.getAttribute('data-desc');

        if (baBeforeImg) baBeforeImg.src = beforeSrc;
        if (baAfterImg) baAfterImg.src = afterSrc;
        if (baProjectTitle) baProjectTitle.textContent = title;
        if (baProjectDesc) baProjectDesc.textContent = desc;

        setSliderPos(50);
        updateImageDimensions();
      });
    });

    // Auto-Scan Reveal Animation Toggle
    const startAutoScan = () => {
      isScanning = true;
      if (baAutoScanBtn) {
        baAutoScanBtn.innerHTML = '<span class="scan-icon">⏸</span> Pause Auto-Scan';
      }
      scanInterval = setInterval(() => {
        scanPos += scanDirection * 0.8;
        if (scanPos >= 90) scanDirection = -1;
        if (scanPos <= 10) scanDirection = 1;
        setSliderPos(scanPos);
      }, 16);
    };

    const stopAutoScan = () => {
      isScanning = false;
      if (scanInterval) clearInterval(scanInterval);
      if (baAutoScanBtn) {
        baAutoScanBtn.innerHTML = '<span class="scan-icon">▶</span> Auto-Scan Reveal';
      }
    };

    if (baAutoScanBtn) {
      baAutoScanBtn.addEventListener('click', () => {
        if (isScanning) {
          stopAutoScan();
        } else {
          startAutoScan();
        }
      });
    }

    // Auto-start initial scan hint for 3 seconds then center
    setTimeout(() => {
      if (!isDragging && !isScanning) {
        let hintCount = 0;
        const hintTimer = setInterval(() => {
          hintCount += 0.05;
          const hintPos = 50 + Math.sin(hintCount * 4) * 20;
          setSliderPos(hintPos);
          if (hintCount >= Math.PI * 2) {
            clearInterval(hintTimer);
            setSliderPos(50);
          }
        }, 16);
      }
    }, 1000);
  }
});
