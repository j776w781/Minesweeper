import os
import pandas as pd

FILEPATH = '../Minesweeper-TEAM6-UPDATES/leaderboard/leaderboard.csv'

class Leaderboard:
    def __init__(self):
        self.data = []
    
    def log_time(self, element):
        self.data.append(element)
        self.data.sort(reverse = True)
        self.save_time('leaderboard')

    def save_time(self,output_dir):
        # Save leaderboard to CSV
        os.makedirs(output_dir, exist_ok=True)
        if len(self.data ) < 5:
            df = pd.DataFrame(self.data[:len(self.data)])
        else:
            df = pd.DataFrame(self.data[:10])
        csv_path = os.path.join(output_dir, 'leaderboard.csv')
        df.to_csv(csv_path, index=False)

    def read(self):
        self.data = []
        filepath = FILEPATH
        try:
            with open(filepath, 'r') as file: # Open the file in read mode ('r')
                lines = file.readlines()# Read all lines from the file
                # Process each line: strip whitespace (especially the newline '\n')
                for line in lines:
                    clean_line = line.strip()
                    if clean_line: # Only add non-empty lines
                        self.data.append(int(clean_line))
            return self.data
            
        except FileNotFoundError:
            print(f"Error: The file at path '{filepath}' was not found.")
            return []
        except Exception as e:
            print(f"An unexpected error occurred while reading the file: {e}")
            return []
    
    def parse(self):
        parsed = []
        for line in self.data:
            try:
                parsed.append(int(line.strip()))
            except ValueError:
                print(f"Skipping malformed line: '{line}'")
        self.data = parsed
        return self.data
        
    def update(self, entry):
        self.read()
        filepath = FILEPATH
        
        self.data = self.data + [entry]
        self.leaderboard = self.data.sort(reverse=False)
        try:
            with open(filepath, 'w') as file:
                for entry in self.data:
                    line = entry
                    file.write(line + '\n')
            print(f"Successfully updated leaderboard and saved {len(self.data)} entries to {filepath}.")
            
        except Exception as e:
            print(f"Error writing to file: {e}")

        return self.leaderboard
