


seeds_dir = "res/seeds/"
seeds_file = seeds_dir + "animate.txt"


animates = list()

with open(seeds_file, mode="r", encoding="utf-8") as seeds:
    with open(seeds_dir + "animate_nodupl.txt", mode="w", encoding="utf-8") as new:
        for line in seeds:
            animates.append(line)

        sorted_anim = sorted(animates)
        sorted_anim_without_dupl = set(sorted_anim)

        for anim in sorted_anim_without_dupl:
            new.write(anim)

print("Fin")



