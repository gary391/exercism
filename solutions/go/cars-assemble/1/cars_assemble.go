package cars

import "fmt"

// CalculateWorkingCarsPerHour calculates how many working cars are
// produced by the assembly line every hour.
func CalculateWorkingCarsPerHour(productionRate int, successRate float64) float64 {
    rate := successRate / float64(100)
    return float64(productionRate) * rate
	// panic("CalculateWorkingCarsPerHour not implemented")
}

// CalculateWorkingCarsPerMinute calculates how many working cars are
// produced by the assembly line every minute.
func CalculateWorkingCarsPerMinute(productionRate int, successRate float64) int {
    s_rate := successRate / float64(100)
    p_rate := float64(productionRate) / 60 
    return int(p_rate  * s_rate)
	// panic("CalculateWorkingCarsPerMinute not implemented")
}

// CalculateCost works out the cost of producing the given number of cars.
func CalculateCost(carsCount int) uint {
    if carsCount >= 10 {
        //check 
        if carsCount % 10 == 0  {
        	return uint(carsCount * 9500)
        } else {
        	cost_1 := carsCount % 10
        	fmt.Printf("cost_1: %+v \n" ,cost_1)
    		cost_2 := int(carsCount / 10)
            fmt.Printf("cost_2: %+v \n" ,cost_2)
   			return uint((cost_1) * 10000 + int(cost_2) * 95000)
    		}
        } else {
            return uint(carsCount) * 10000
        }
    }


