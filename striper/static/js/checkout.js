// Listener for buy button
const buyProduct = (buyBtn, url) => {
    const apiKey = document.getElementById('apiKey')
    const stripe = Stripe(apiKey.getAttribute('data-key'));

    fetch(url)
        .then(res => res.json())
        .then(data => {
            return stripe.redirectToCheckout({ sessionId: data.key })
        })
        .then(function (result) {
          if (result.error) {
            alert(result.error.message);
          }
        })
        .catch(function (error) {
          console.error("Error:", error);
        });
}
