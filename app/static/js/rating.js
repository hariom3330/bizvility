// star-rating.js

document.addEventListener('DOMContentLoaded', function() {
    var starRatingElements = document.querySelectorAll('.star-rating');

    starRatingElements.forEach(function(starRatingElement) {
        var rating = parseFloat(starRatingElement.getAttribute('data-rating'));
        starRatingElement.style.setProperty('--rating', rating);
    });
});
