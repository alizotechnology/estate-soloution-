const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Serve public static assets
app.use('/assets', express.static(path.join(__dirname, 'public/assets')));

// Clean route handlers
const routes = {
  '/': 'index.html',
  '/projects': 'projects/index.html',
  '/buy-sell': 'buy-sell/index.html',
  '/gallery': 'gallery/index.html',
  '/contact': 'contact/index.html',
  '/takmeel-square': 'takmeel-square/index.html',
  '/pelican-mall': 'pelican-mall/index.html',
  '/defence-gardenia-villas': 'defence-gardenia-villas/index.html',
  '/about': 'about/index.html',
  '/services': 'services/index.html',
  '/faq': 'faq/index.html',
  '/privacy-policy': 'privacy-policy/index.html',
  '/terms': 'terms/index.html'
};

Object.entries(routes).forEach(([routePath, filePath]) => {
  app.get(routePath, (req, res) => {
    res.sendFile(path.join(__dirname, filePath));
  });
  if (routePath !== '/') {
    app.get(`${routePath}/`, (req, res) => {
      res.sendFile(path.join(__dirname, filePath));
    });
  }
});

app.use(express.static(__dirname));

// Fallback to home page or custom 404
app.use((req, res) => {
  res.status(404).sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
  console.log(`Estate Solutions Portal running on http://localhost:${PORT}`);
});
