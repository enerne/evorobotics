from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for key in self.parents.keys():
            child = copy.deepcopy(self.parents[key])
            child.Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

            self.children[key] = child

    def Mutate(self):
        for child in self.children.values():
            child.Mutate()

    def Evaluate(self, solutions):
        for sol in solutions.values():
            sol.Start_Simulation("DIRECT")

        for parent in solutions.values():
            parent.Wait_For_Simulation_To_End()




    def Select(self):
        for k in self.parents.keys():
            if self.parents[k].fitness > self.children[k].fitness:
                self.parents[k] = self.children[k]
    def Show_Best(self):
        winner = self.parents[0]
        for p in self.parents.values():
            if p.fitness < winner.fitness:
                winner = p
        p.Start_Simulation("GUI")
        print(p.fitness)

    def Print(self):
        print()
        for k in self.parents.keys():
            p = self.parents[k]
            c = self.children[k]
            print(p.fitness,c.fitness)

        print()