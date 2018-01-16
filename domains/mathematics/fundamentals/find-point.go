package main

import "fmt"

func main(){
	var T int
	fmt.Scan(&T)
	for i := 0; i < T; i++ {
		var px int
		var py int
		var qx int
		var qy int
		fmt.Scan(&px, &py, &qx, &qy)
		fmt.Println((qx-px) + qx, (qy-py) + qy)
	}
}