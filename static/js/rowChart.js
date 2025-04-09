document.addEventListener('DOMContentLoaded', function() {
const ctx = document.getElementById('rowChart').getContext('2d');

const rowChart = new Chart(ctx, {
    type: 'bar',
    data: {
    labels: [
        "Graphic design",
        "Asset Management",
        "Service Now",
        "Microsoft 365",
        "Active Directory",
        "Technical Support"
    ],
    datasets: [{
        label: 'Other Skills',
        data: [16, 11, 13, 14, 12, 15],
        backgroundColor: '#486d67',
        borderColor: '#486d67',
        borderWidth: 1
    }]
    },
    options: {
    indexAxis: 'y', 
    scales: {
        x: {
        beginAtZero: true
        }
    },
    responsive: true,
    plugins: {
        legend: {
        display: false
        },
        title: {
        display: true,
        text: 'Other Skills Row Chart'
        }
    }
    }
});
});