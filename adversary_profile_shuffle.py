import yaml
import os
import sys
import random

def rename_yaml(input_file, number):
    # Read File Input
    with open(input_file, 'r') as file:
        data = yaml.safe_load(file)

    # Extract the previous name from the YAML data
    previous_name = data.get('name')

    if previous_name:
        new_name = f"{previous_name}_Adversary_Profile_{number}"
        new_file_name = f"{new_name}.yaml"

        # Update the name in the data
        data['name'] = new_name

        # Extract steps
        steps = data['atomic_ordering']

        # Organize steps into groups
        step_groups = []
        curr_group = []
        prev_tactic = None
        for step in steps:
            curr_tactic = data['abilities'][step]['tactic']

            if prev_tactic is None or curr_tactic == prev_tactic:
                curr_group.append(step)
                
            else:
                step_groups.append(curr_group)
                curr_group = [step]

            prev_tactic = curr_tactic
        step_groups.append(curr_group)

        # Randomize groups 
        final_order = []
        for group in step_groups:
            random.shuffle(group)
            final_order.extend(group)

        data['atomic_ordering'] = final_order

        # Write the modified data to a new YAML file
        with open(new_file_name, 'w') as new_file:
            yaml.dump(data, new_file, default_flow_style=False, sort_keys=False)

        print(f"Renamed '{previous_name}' to '{new_name}' and saved as '{new_file_name}'.")
    else:
        print("No 'name' field found in the YAML file.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python adversary_profile_shuffle.py [path_to_adversary_profile] [number_of_variants]")
        sys.exit(1)

    input_yaml_file = sys.argv[1]
    number_of_variants = int(sys.argv[2])

    for i in range(1, number_of_variants + 1):
        rename_yaml(input_yaml_file, i)
