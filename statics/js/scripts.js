function showSection(sectionId) {
  // Hide all sections
  const sections = document.querySelectorAll('.content-section');
  sections.forEach(section => section.classList.remove('active'));

  // Show selected section
  document.getElementById(sectionId).classList.add('active');

  // Update active nav link
  const navLinks = document.querySelectorAll('.nav-link');
  navLinks.forEach(link => link.classList.remove('active'));
  event.target.classList.add('active');
}

// Navbar scroll effect
document.addEventListener('DOMContentLoaded', function() {
  window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar-custom');
    if (window.scrollY > 50) {
      navbar.style.background = 'rgba(255, 255, 255, 0.35)';
      navbar.style.backdropFilter = 'blur(20px)';
    } else {
      navbar.style.background = 'rgba(255, 255, 255, 0.25)';
      navbar.style.backdropFilter = 'blur(15px)';
    }
  });
});
