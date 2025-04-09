document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('radarChart').getContext('2d');

    const radarChart = new Chart(ctx, {
    type: 'radar',
    data: {
        labels: ["PYTHON",  "REACT", "JAVASCRIPT", "DJANGO","CSS","HTML"],
        datasets: [
        {
            label: "2024-Oct",
            data: [0, 0, 3, 0, 7, 8],
            borderColor: "#7e468a",
            backgroundColor: "rgba(126, 70, 138, 0.2)",
            fill: true
        },
        {
            label: "2024-Nov",
            data: [2, 5, 6, 0, 6, 6],
            borderColor: "#635a92",
            backgroundColor: "rgba(99, 90, 146, 0.2)",
            fill: true
        },
        {
            label: "2024-Dec",
            data: [3, 6, 6, 4, 7, 7],
            borderColor: "#506e9a",
            backgroundColor: "rgba(80, 110, 154, 0.2)",
            fill: true
        },
        {
            label: "2025-Jan",
            data: [4, 6, 6, 7, 7, 8],
            borderColor: "#2d8bba",
            backgroundColor: "rgba(45, 139, 186, 0.2)",
            fill: true
        },
        {
            label: "2025-Feb",
            data: [5, 6, 6, 7, 7, 9],
            borderColor: "#00bf63",
            backgroundColor: "rgba(12, 138, 77, 0.2)",
            fill: true
        },
        {
            label: "2025-Mar",
            data: [6, 7, 7, 8, 8, 9],
            borderColor: "#5271ff",
            backgroundColor: "rgba(199, 119, 252, 0.2)",
            fill: true
        }
        ]
    },
    options: {
        responsive: true,
        scales: {
        r: {
            beginAtZero: true,
            suggestedMax: 10,
            pointLabels: {
            font: {
                size: 16
            }
            }
        }
        },
        plugins: {
        legend: {
            position: 'top'
        },
        title: {
            display: true,
            text: 'Technology Progress Chart'
        }
        }
    }
    });
});