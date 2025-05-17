document.addEventListener('DOMContentLoaded', function() {
  const navLinks = document.querySelectorAll('.app-nav a');
  const currentPath = window.location.pathname;

  navLinks.forEach(link => {
    if (link.getAttribute('href') && currentPath.includes(link.getAttribute('href').split('/').pop())) {
      if (link.getAttribute('href') === "{{ url_for('dashboard') }}" && (currentPath === '/' || currentPath.endsWith('/dashboard'))) {
        link.classList.add('active');
      } else if (link.getAttribute('href').endsWith(currentPath.substring(currentPath.lastIndexOf('/')))) {
        link.classList.add('active');
      }
    }
    if (link.href.includes('mahasiswa') && currentPath.includes('mahasiswa')) {
      if (link.getAttribute('href').endsWith('mahasiswa')) {
        link.classList.add('active');
      }
    }
  });

  if (!document.querySelector('.app-nav a.active')) {
    navLinks.forEach(link => {
      const linkPath = link.pathname;
      if (currentPath === linkPath || (linkPath !== '/' && currentPath.startsWith(linkPath))) {
        link.classList.add('active');
      }
    });
  }

  const footerYearElement = document.querySelector('.app-footer p');
  if (footerYearElement) {
    const currentFooterText = footerYearElement.textContent;
    const yearMatch = currentFooterText.match(/©\s*(\d{4})\s*\{\{.*?\}\}.*My Simple Flask App/);

    if (yearMatch) {
      const yearPlaceholder = yearMatch[1];
      const currentYear = new Date().getFullYear();
      if (yearPlaceholder.startsWith("{{") || parseInt(yearPlaceholder) !== currentYear) {
        footerYearElement.textContent = `© ${currentYear} My Simple Flask App`;
      }
    } else {
      footerYearElement.textContent = `© ${new Date().getFullYear()} My Simple Flask App`;
    }
  }

  const formInputs = document.querySelectorAll('.form-group input[type="text"], .form-group input[type="password"], .form-group input[type="email"]');
  formInputs.forEach(input => {
    input.addEventListener('focus', () => {
      input.parentElement.classList.add('is-focused');
    });
    input.addEventListener('blur', () => {
      input.parentElement.classList.remove('is-focused');
    });
  });
});
