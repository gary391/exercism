// Package weather provides a forecast based on the current location and condition.
package weather


var (
	// CurrentCondition represents a location and condition in string format.
    CurrentCondition string
    // CurrentLocation represents a location and condition in string format.
	CurrentLocation  string
)

// Forecast returns a string which is an concatenation of current location and 
// current condition at that location.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
