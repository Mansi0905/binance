const ctx = document.getElementById('priceChart').getContext('2d');
const chart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    datasets: [{
      label: 'BTC Price',
      data: [10000, 10500, 10200, 11000, 10700],
      borderColor: '#f0b90b',
      borderWidth: 2,
      fill: false,
    }]
  },
  options: {
    backgroundColor: '#0b0e11',
    plugins: {
      legend: { labels: { color: '#fff' } }
    },
    scales: {
      x: { ticks: { color: '#fff' } },
      y: { ticks: { color: '#fff' } }
    }
  }
});
