// Optional: Add simple client-side validation or interactivity
document.getElementById('calorieForm').addEventListener('submit', function() {
    alert("Calculating Calories Burned...");
});
document.getElementById("calorieForm").addEventListener("submit", function(e) {
    let heightValue = parseFloat(document.getElementById("heightInput").value);
    let heightUnit = document.getElementById("heightUnit").value;
    let heightCm;

    if (isNaN(heightValue)) {
        alert("Please enter a valid height");
        e.preventDefault();
        return;
    }

    switch(heightUnit) {
        case "cm":
            heightCm = heightValue;
            break;
        case "m":
            heightCm = heightValue * 100;
            break;
        case "ft":
            heightCm = heightValue * 30.48;
            break;
        case "inch":
            heightCm = heightValue * 2.54;
            break;
    }

    // Update the input value to cm before submitting the form
    document.getElementById("heightInput").value = heightCm.toFixed(2);
});
