import yaml
import sys

# Function to extract and format attack_id from YAML file
def extract_attack_ids(adversary_profile, num):

    attack_ids = f'\npath_{num}:'

    with open(adversary_profile, 'r') as file:
        # Load YAML content from adversary_profile file
        adversary_data = yaml.safe_load(file)   

    with open(emulation_plan, 'r') as file:
        # Load YAML content from adversary_profile file
        emulation_data = yaml.safe_load(file)         
        
    # Get the order of the steps
    atomic_ordering = adversary_data.get('atomic_ordering')
    abilities = adversary_data.get('abilities')

    # Get extended info about each step
    def emulation_info(step_id):
        for step in emulation_data:
            if(step.get('id') == step_id):
                return step

    # Iterate through each step in the atomic ordering
    for step_id in atomic_ordering:

        step_info = emulation_info(step_id)
        attack_id = step_info.get('technique').get('attack_id')
        tactic = step_info.get('tactic')
    
        platforms = step_info.get('platforms')

        for os, shells in platforms.items():
            for shell, inputs in shells.items():
                payloads = inputs.get('payloads') or []

        output = f'{attack_id} # {tactic}'

        # print out name of payloads
        if not (payloads == []):
            for payload in payloads:
                output += f' - {payload}'

        # print out that it needs payloads
        if not (payloads == []):
            output += ' - (requires its payload)'
            attack_ids += (f'\n  - {attack_id}_payload')
        attack_ids += (f'\n  - {output}')

    return attack_ids

        # # List to hold all formatted attack_ids
        # attack_ids = []
        
        # # Variable to store the immediate previous step's payload
        # previous_payload = None
        # payload_appended = False  # To ensure a payload is appended only once
        # privilege_escalation = False  # Flag to track privilege escalation stepsp
        # requires_payload_steps = set()  # Set to track steps that require payloads
        
        # # List of tactics related to privilege escalation
        # privilege_escalation_tactics = {'privilege escalation', 'elevation of privilege'}

        # Traverse through the data and collect attack_ids
        # for atomic_id, item in atomic_ordering.items():        
            
        #     # Check if the current step has payloads
        #     has_payloads = 'payloads' in cmd
        #     current_payloads = cmd.get('payloads', [])
            
        #     # Check if the current tactic involves privilege escalation
        #     if tactic in privilege_escalation_tactics:
        #         privilege_escalation = True
            
        #     if attack_id:
        #         marked_payload = False
        #         if has_payloads:
        #             # Add _payload if 'payloads' is present
        #             attack_id += '_payload'
        #             # Store the current payloads
        #             if current_payloads:
        #                 previous_payload = current_payloads[-1]  # Use the last payload
        #                 payload_appended = False  # Reset payload appended flag
        #         else:
        #             # Append the previous payload if available and not already appended
        #             if previous_payload and not payload_appended:
        #                 attack_id += f' # {tactic} - {previous_payload}'
        #                 payload_appended = True  # Mark that payload has been appended
        #                 marked_payload = True
        #             else:
        #                 attack_id += f' # {tactic}'
                    
        #             # Append (requires 
        # return attack_ids
def get_name(): 
    with open(emulation_plan, 'r') as file:
        # Load YAML content from adversary_profile file
        emulation_data = yaml.safe_load(file)  
    return(emulation_data[0].get('emulation_plan_details').get('adversary_name'))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python process_attack_ids.py [path_to_emulation_plan] [path_to_adversary_profile(s)...]" )
        sys.exit(1)

    emulation_plan = sys.argv[1]
    adversary_profiles = sys.argv[2:]


    processed_file = open(f'{get_name()}_Processed_Attack_IDS.yaml', "w") 
    for i in range(len(adversary_profiles)):
        processed_file.write(extract_attack_ids(adversary_profiles[i], i+1))
        print(f'Wrote {adversary_profiles[i]} as path_{i+1}')
    processed_file.close()
    print(f'Finished {get_name()}_Processed_Attack_IDS.yaml')