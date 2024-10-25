# Adversary_Profile

The adversary profile is yaml file you get from exporting adversary from the Caldera WebUI. You can export an adversary profile by clicking the export button. This contains the ordering of the steps to be executed and can be reimported in the same page. However this profile does not have all the information regarding each campaign, to get the full picture we need an Emulation Plan.

![](/Adversary.png)

# Emulation Plan

The Emulation plan is a yaml file that can be found within the adversary_emulation_library Github Repo. This repo is imported into Caldera through a script but its easier to find the files [online](https://github.com/center-for-threat-informed-defense/adversary_emulation_library). Within each adversary is an /Emulation_Plan folder which contains the file and has information that will support processing the Adversary Profile.

![](/Emulation.png)


# adversary_profile_shuffle.py

Usage: python adversary_profile_shuffle.py [path_to_adversary_profile] [number_of_variants]  
Intakes an adversary profile and shuffles the order into X number of variants according to certain rules.

```
kevin@home-desktop:~$ python adversary_profile_shuffle.py OilRig_Adversary_Profile.yaml 3
Renamed 'OilRig' to 'OilRig_Adversary_Profile_1' and saved as 'OilRig_Adversary_Profile_1.yaml'.
Renamed 'OilRig' to 'OilRig_Adversary_Profile_2' and saved as 'OilRig_Adversary_Profile_2.yaml'.
Renamed 'OilRig' to 'OilRig_Adversary_Profile_3' and saved as 'OilRig_Adversary_Profile_3.yaml'.
```

# process_attack_ids.py

Usage: python process_attack_ids.py [path_to_emulation_plan] [path_to_adversary_profile(s)...]  
Intakes an emulation plan and an arbitrary numebr of adversary profiles. Compiles all their ids into a yaml file with some other information.

```
kevin@home-desktop:~$ python process_attack_ids.py OilRig_Emulation_Plan.yaml OilRig_Adversary_Profile_1.yaml OilRig_Adversary_Profile_2.yaml OilRig_Adversary_Profile_3.yaml 
Wrote OilRig_Adversary_Profile_1.yaml as path_1
Wrote OilRig_Adversary_Profile_2.yaml as path_2
Wrote OilRig_Adversary_Profile_3.yaml as path_3
Finished OilRig_Processed_Attack_IDS.yaml
```



