def calculateAvgVelocity(Sprint_points):
    total_points=0
    for i in Sprint_points:
        total_points+=int(i)
    return(total_points/len(Sprint_points))

def FeatureOneInputs():
    sp=input("enter story points for each sprint (seperated by space)\n")
    Sprint_points=sp.split(" ")
    return Sprint_points

class TeamMember:
    def __init__(self, memberid=0, minDailyHours=0, maxDailyHours=0, ceremonyHours=0, daysOff=0):
        self.memberId = memberid
        self.minDailyHours = minDailyHours
        self.maxDailyHours = maxDailyHours
        self.ceremonyHours = ceremonyHours
        self.daysOff = daysOff
        
    def calculateIndividualCapacity(self, members, sprintLength):
         
        minCapacities = [0.0] * len(members)
        maxCapacities = [0.0] * len(members)
        for i in range(len(members)):
            availableDays = sprintLength - members[i].daysOff
            minAvailableHours = availableDays * (members[i].minDailyHours - members[i].ceremonyHours)
            maxAvailableHours = availableDays * (members[i].maxDailyHours - members[i].ceremonyHours)
            minCapacities[i] = minAvailableHours
            maxCapacities[i] = maxAvailableHours
        print("Sprint Length: " + str(sprintLength))
        print("Team Size: " + str(len(members)))
        capacities = {}
        capacities["minimum"] = minCapacities
        capacities["maximum"] = maxCapacities
        self.printIndividualCapacities(members, capacities)
        return capacities
    
    def calculateTeamCapacity(self, individualCapacities):
        minTeamCapacity = 0
        maxTeamCapacity = 0
        minCapacities = individualCapacities["minimum"]
        for capacity in minCapacities:
            minTeamCapacity += capacity
        maxCapacities = individualCapacities["maximum"]
        for capacity in maxCapacities:
            maxTeamCapacity += capacity
        teamCapacityRange = str(minTeamCapacity) + " - " + str(maxTeamCapacity)
        return teamCapacityRange
    
    def printIndividualCapacities(self, members, capacityMap):
        if members is None or len(members) == 0:
            return
        print("Member ID--", "Daily Hours--", "Ceremony Hours--", "Days Off--", "Available Effort-Hours range")
        i = 0
        minCapacities = capacityMap["minimum"]
        maxCapacities = capacityMap["maximum"]
        for entry in members:
            effortHoursRange = str(minCapacities[i]) + " - " + str(maxCapacities[i])
            dailyHourRange = str(entry.minDailyHours) + " - " + str(entry.maxDailyHours)
            print(entry.memberId,"----" , dailyHourRange,"----" , entry.ceremonyHours,"----" , entry.daysOff,"----" , effortHoursRange)
            i += 1


        
def FeatureTwoInputs():
    sprintDays = int(input("\n\nEnter the length ofsprint: "))
    memberNum = int(input("Enter the number of team members: "))
    teamMemberDetails = []
    for i in range(1, memberNum+1):
        print("\nMember " + str(i))
        memberid = int(input("Member Id: "))
        hoursPerDay = input("enter availablity hours per day as a range: ")
        sprintCeremonyTime = float(input("daily hours spent in Sprint Ceremonies: "))
        daysOff = float(input("No of days off during the sprint: "))
        minHours = float(hoursPerDay.split("-")[0].strip())
        maxHours = float(hoursPerDay.split("-")[1].strip())
        member = TeamMember(memberid, minHours, maxHours, sprintCeremonyTime, daysOff)
        teamMemberDetails.append(member)
    return(teamMemberDetails,sprintDays)
    
    
if __name__ == "__main__":
    
       Sprint_points = FeatureOneInputs()
       avg_velocity=calculateAvgVelocity(Sprint_points)
       print("Average velocity = ",avg_velocity)
       teamMemberDetails,sprintDays =FeatureTwoInputs()
       memberObj = TeamMember()
       memberCapacities = memberObj.calculateIndividualCapacity(teamMemberDetails, sprintDays)
       teamCapacity = memberObj.calculateTeamCapacity(memberCapacities)
       

       
       
        
