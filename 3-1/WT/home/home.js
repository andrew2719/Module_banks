function searchCourses() {
    const searchTerm = document.getElementById('searchInput').value;
    if (searchTerm) {
        // In a real-world scenario, you'd use this searchTerm to query your database or search algorithm.
        alert('Searching for courses related to: ' + searchTerm);
    } else {
        alert('Please enter a search term.');
    }
}
