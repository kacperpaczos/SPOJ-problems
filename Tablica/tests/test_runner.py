#!/usr/bin/env python3
"""
Test runner utility for executing TABLICA solutions.

Provides a unified interface for running Python, Java, and C++ solutions
with input data and capturing their output.
"""

import subprocess
import sys
import os
from typing import Tuple


class SolutionRunner:
    """Runner class for executing solutions in different languages."""

    def __init__(self, solutions_dir: str = "solutions"):
        """
        Initialize runner with solutions directory.

        Args:
            solutions_dir: Path to directory containing solution files
        """
        # Get absolute path relative to project root
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(script_dir)
        self.solutions_dir = os.path.join(project_root, solutions_dir)
        
        self.solutions = {
            'python': os.path.join(self.solutions_dir, 'tablica.py'),
            'java': os.path.join(self.solutions_dir, 'Tablica.java'),
            'cpp': os.path.join(self.solutions_dir, 'tablica.cpp')
        }
        
        # Ensure solutions directory exists
        if not os.path.exists(self.solutions_dir):
            raise FileNotFoundError(f"Solutions directory not found: {self.solutions_dir}")
        
        # Verify solution files exist
        for lang, path in self.solutions.items():
            if not os.path.exists(path):
                raise FileNotFoundError(f"{lang} solution not found: {path}")

    def run(self, language: str, input_data: str, timeout: int = 10) -> Tuple[str, str, int]:
        """
        Run a solution with given input data.

        Args:
            language: One of 'python', 'java', 'cpp'
            input_data: Input string to feed to the program
            timeout: Maximum execution time in seconds

        Returns:
            Tuple of (stdout, stderr, return_code)

        Raises:
            ValueError: If language is not supported
            subprocess.TimeoutExpired: If execution exceeds timeout
        """
        if language not in self.solutions:
            raise ValueError(f"Unknown language: {language}. Supported: {list(self.solutions.keys())}")

        file_path = self.solutions[language]

        if language == 'python':
            return self._run_python(file_path, input_data, timeout)
        elif language == 'java':
            return self._run_java(file_path, input_data, timeout)
        elif language == 'cpp':
            return self._run_cpp(file_path, input_data, timeout)

    def _run_python(self, file_path: str, input_data: str, timeout: int) -> Tuple[str, str, int]:
        """Run Python solution."""
        cmd = [sys.executable, file_path]
        
        result = subprocess.run(
            cmd,
            input=input_data,
            text=True,
            capture_output=True,
            timeout=timeout
        )
        
        return result.stdout.strip(), result.stderr.strip(), result.returncode

    def _run_java(self, file_path: str, input_data: str, timeout: int) -> Tuple[str, str, int]:
        """Run Java solution (compile if needed, then execute)."""
        class_name = os.path.splitext(os.path.basename(file_path))[0]
        class_file = os.path.join(self.solutions_dir, f"{class_name}.class")
        
        # Check if compilation is needed
        if not os.path.exists(class_file) or \
           os.path.getmtime(file_path) > os.path.getmtime(class_file):
            # Compile
            compile_cmd = ['javac', file_path]
            compile_result = subprocess.run(
                compile_cmd,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            
            if compile_result.returncode != 0:
                return "", f"Compilation error: {compile_result.stderr}", compile_result.returncode
        
        # Run
        run_cmd = ['java', '-cp', self.solutions_dir, class_name]
        result = subprocess.run(
            run_cmd,
            input=input_data,
            text=True,
            capture_output=True,
            timeout=timeout
        )
        
        return result.stdout.strip(), result.stderr.strip(), result.returncode

    def _run_cpp(self, file_path: str, input_data: str, timeout: int) -> Tuple[str, str, int]:
        """Run C++ solution (compile if needed, then execute)."""
        exe_path = os.path.join(self.solutions_dir, 'tablica_exe')
        
        # Check if compilation is needed
        if not os.path.exists(exe_path) or \
           os.path.getmtime(file_path) > os.path.getmtime(exe_path):
            # Compile
            compile_cmd = ['g++', '-std=c++17', '-O2', '-o', exe_path, file_path]
            compile_result = subprocess.run(
                compile_cmd,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            
            if compile_result.returncode != 0:
                return "", f"Compilation error: {compile_result.stderr}", compile_result.returncode
        
        # Run
        result = subprocess.run(
            [exe_path],
            input=input_data,
            text=True,
            capture_output=True,
            timeout=timeout
        )
        
        return result.stdout.strip(), result.stderr.strip(), result.returncode


if __name__ == "__main__":
    # Simple test of the runner
    runner = SolutionRunner()
    
    print("Testing SolutionRunner...")
    test_input = "1 2 3"
    expected_output = "3 2 1"
    
    for lang in ['python', 'java', 'cpp']:
        stdout, stderr, code = runner.run(lang, test_input)
        status = "✓" if stdout == expected_output and code == 0 else "✗"
        print(f"{status} {lang}: {stdout} (exit code: {code})")
        if stderr:
            print(f"  stderr: {stderr}")
