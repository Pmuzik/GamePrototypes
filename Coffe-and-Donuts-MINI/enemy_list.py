#enemy_list
from Characters import Enemy
e_dict = {'common': [Enemy('Goblin', 1000, 1000, 150, 150, {"strike":{"Power": range(1,10), "MP Cost": 0}, "goblin-fire":{"Power": range(25,35), "MP Cost": 70}}, {}),
			Enemy('Orc', 1500, 1500, 50, 50, {"strike":{"Power": range(1,10), "MP Cost": 0}, 'horn':{"Power": range(10,15), "MP Cost": 0}, "axe-swing": {"Power": range(1,50), "MP Cost": 0}}, {}),
			Enemy('Slime', 500, 500, 500, 500, {"fire":{"Power": range(15, 25), "MP Cost": 0}}, {})],
			'uncommon': [Enemy('Mindflayer', 750, 750, 1000, 1000, {"strike":{"Power": range(1,10), "MP Cost": 0}, "flare":{"Power": range(50, 100), "MP Cost": 50}, 
				"scourge":{"Power": range(100, 500), "MP Cost": 90}, "mindlash":{"Power": range(10,50), "MP Cost": 5}}, {}),
						Enemy('Bandersnatch', 2000, 2000, 200, 200,{"strike":{"Power": range(1,10), "MP Cost": 0}, "psi-claw":{"Power": range(25,60), "MP Cost": 5}}, {}),
						Enemy('Ice-Wyrm', 2500, 2500, 1000, 1000,{"strike":{"Power": range(1,10), "MP Cost": 0}, "ice-breath":{"Power": range(1, 500), "MP Cost": 50}}, {})],
			'rare': [Enemy('Xagor the Mad', 9999, 9999, 9999, 9999,{'tentacle':{"Power":range(50,65), "MP Cost": 0},"flare":{"Power": range(50, 100), "MP Cost": 50}, "X-Virus":{"Power": range(1, 999), 
				"MP Cost": 900}}, {})]
			}