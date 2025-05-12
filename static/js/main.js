// Динамическое обновление времени бронирования
document.addEventListener('DOMContentLoaded', function() {
    // Обработчик изменения даты
    const startDateInput = document.getElementById('id_start_time');
    const endDateInput = document.getElementById('id_end_time');

    if (startDateInput && endDateInput) {
        startDateInput.addEventListener('change', function() {
            // Автоматически устанавливаем конечное время = начальное + 1 час
            const startTime = new Date(this.value);
            const endTime = new Date(startTime.getTime() + 60*60*1000);
            endDateInput.value = endTime.toISOString().slice(0, 16);
        });
    }

    // Подтверждение отмены брони
    document.querySelectorAll('.cancel-booking').forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to cancel this booking?')) {
                e.preventDefault();
            }
        });
    });
});

// AJAX-проверка доступности времени
function checkAvailability(roomId, startTime, endTime) {
    fetch(`/api/check_availability/?room=${roomId}&start=${startTime}&end=${endTime}`)
        .then(response => response.json())
        .then(data => {
            if (data.available) {
                document.getElementById('availability-status').innerHTML =
                    '<div class="alert alert-success">Time slot available!</div>';
            } else {
                document.getElementById('availability-status').innerHTML =
                    '<div class="alert alert-danger">Time slot occupied!</div>';
            }
        });
}