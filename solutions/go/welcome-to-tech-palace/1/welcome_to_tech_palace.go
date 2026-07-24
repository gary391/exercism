package techpalace
import "strings"

// WelcomeMessage returns a welcome message for the customer.
func WelcomeMessage(customer string) string {
    return "Welcome to the Tech Palace, " + strings.ToUpper(customer) 
	// panic("Please implement the WelcomeMessage() function")
}

// AddBorder adds a border to a welcome message.
func AddBorder(welcomeMsg string, numStarsPerLine int) string {
	stars := strings.Repeat("*", numStarsPerLine)
    return stars + "\n" + welcomeMsg + "\n" + stars
    // fmt.Println ("Example: " + star +"\n Welcome! \n" + star)
    // panic("Please implement the AddBorder() function")
    
}

// CleanupMessage cleans up an old marketing message.
func CleanupMessage(oldMsg string) string {
    noStars := strings.ReplaceAll(oldMsg, "*", "")
    
    // 2. Remove all leading and trailing whitespace (including newlines and spaces)
    cleanMsg := strings.TrimSpace(noStars)
    
    return cleanMsg
    
	// panic("Please implement the CleanupMessage() function")
}
