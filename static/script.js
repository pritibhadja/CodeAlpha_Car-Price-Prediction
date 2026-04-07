// Form submit loading state
const form = document.getElementById('predictForm');
const btn = document.getElementById('submitBtn');

if (form && btn) {
    form.addEventListener('submit', () => {
        btn.style.opacity = '0.7';
        btn.style.pointerEvents = 'none';
        btn.querySelector('.btn-text').textContent = 'Estimating...';
    });
}
