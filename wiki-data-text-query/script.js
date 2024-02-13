document.getElementById('runQuery').addEventListener('click', function() {
    const query = document.getElementById('queryBox').value;
    const resultsContainer = document.getElementById('resultsContainer');
    
    resultsContainer.textContent = 'Loading';
    resultsContainer.style.fontFamily = "Inter";
    
    let dotCount = 1;
    let increasing = true;

    const updateLoadingAnimation = function() {
        // Update dot count
        if (increasing) {
            dotCount++;
            if (dotCount >= 4) {
                increasing = false;
            }
        } else {
            dotCount--;
            if (dotCount <= 1) {
                increasing = true;
            }
        }
        
        resultsContainer.textContent = 'Loading' + '.'.repeat(dotCount);
    };

    const loadingAnimation = setInterval(updateLoadingAnimation, 500);

    fetch('http://127.0.0.1:8000/run-query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: query }),
    })
    .then(response => response.json())
    .then(data => {
        clearInterval(loadingAnimation); // Stop the loading animation
        resultsContainer.textContent = data;
        console.log('Success:', data);

        var sparql_query = data;

        // Encode the query
        var encoded_query = encodeURIComponent(sparql_query);
        var base_url = "https://query.wikidata.org/#";
        var url = base_url + "%20" + encoded_query;

        window.location.href = url;
        console.log("Generated URL:", url);

    })
    .catch((error) => {
        clearInterval(loadingAnimation); // Stop the loading animation
        resultsContainer.textContent = 'Error occurred'; // Display error message
        console.error('Error:', error);
    });
});


document.addEventListener('DOMContentLoaded', function() {
    
    var clearButton = document.getElementById('clearQuery');
    var queryBox = document.getElementById('queryBox');

    clearButton.addEventListener('click', function() {
        queryBox.value = '';
    });
});



