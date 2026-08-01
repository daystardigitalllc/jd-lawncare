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
});
