package main

import (
	"reflect"
	"testing"
)

func Test_twoSum(t *testing.T) {
	testCases := []struct {
		input    []int
		target   int
		expected []int
	}{
		{
			input:    []int{3, 3},
			target:   6,
			expected: []int{0, 1},
		},
	}

	for _, tt := range testCases {
		got := twoSum(tt.input, tt.target)
		if !reflect.DeepEqual(got, tt.expected) {
			t.Errorf("twoSum(%v, %d), expected: %v, got: %v", tt.input, tt.target, tt.expected, got)
		}
	}
}
