package org.example.jython;

import org.python.util.PythonInterpreter;

public class ArrayManager {

    public void maxSubArray() {
        try (PythonInterpreter interpreter = new PythonInterpreter()) {
            interpreter.exec("array = []");
            interpreter.exec("with open(\"input.txt\", 'r') as file:\n" +
                    "\tfor line in file.readlines():\n" +
                    "\t\tarray.extend([int(str_number) for str_number in line.split(\" \")])");

            interpreter.exec("array_of_sub_length = [1]");

            interpreter.exec("print('Array', array)");

            interpreter.exec("for i in range(1, len(array)):\n" +
                    "\tif array[i] >= array[i - 1]:\n" +
                    "\t\tarray_of_sub_length.append(array_of_sub_length[i - 1] + 1)\n" +
                    "\telse:\n" +
                    "\t\tarray_of_sub_length.append(1)");

            interpreter.exec("max_length = max(array_of_sub_length)");
            interpreter.exec("max_length_index = array_of_sub_length.index(max_length)");

            interpreter.exec("print('Result subarray', array[max_length_index - max_length + 1 : max_length_index + 1])");
        }
    }
}
