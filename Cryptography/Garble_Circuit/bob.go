package main

import (
	"crypto/aes"
	"fmt"
)

// Bob the evaluator

func evaluateGarbledCircuit(inputs [][]byte, gates []Gate) []byte {
	n := len(inputs) // number of inputs
	m := len(gates)  // number of gates

	// array of signals have a size of n+m
	signals := make([][]byte, m+n)

	// setup inputs signals
	for i := 0; i < n; i++ {
		signals[i] = inputs[i]
		fmt.Printf("input %d=%x\n", i, signals[i][:2])
	}

	// add code below to evaluate the gates

	//fmt.Print(gates)
	//fmt.Print(signals)
	for _, gate := range gates {
		a := signals[gate.in0]
		b := signals[gate.in1]
		//fmt.Print(a)
		//fmt.Print(b)
		first_a := (a[0]) >> 7
		first_b := (b[0]) >> 7
		o := 0

		if first_a == 0 {
			if first_b == 0 {
				o = 0
			} else {
				o = 1
			}
		} else {
			if first_b == 0 {
				o = 2
			} else {
				o = 3
			}
		}

		cipher, err := aes.NewCipher(append(a, b...))
		if err == nil {
			output := make([]byte, 16)
			for e := range gate.table {
				if e == o {
					cipher.Decrypt(output, gate.table[o])
				}
			}

			signals[gate.out] = output
		}
	}

	// the last signal is the output
	return signals[n+m-1]
}
