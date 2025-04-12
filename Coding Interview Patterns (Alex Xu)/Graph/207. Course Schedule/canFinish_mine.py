class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites:
            return True

        # all visited paths are true because false would terminate the program
        visited_paths = set()

        def dfs(parents, next_course):
            # print(visited_paths, parents, next_course)
            for curr_arr_2 in prerequisites:
                if curr_arr_2[0] == next_course:
                    curr_path = str(curr_arr_2[0]) + "-" + str(curr_arr_2[1])

                    # add parent before testing for cases:[[5,5]]
                    parents.add(curr_arr_2[0])
                    if curr_arr_2[1] in parents:
                        # print("in false")
                        return False

                    if curr_path in visited_paths:
                        # print("skip")
                        continue
                    else:
                        visited_paths.add(curr_path)

                    # True case
                    # print("in add")                       
                    next_course = curr_arr_2[1]
                    return dfs(parents, next_course)                       

        for curr_arr in prerequisites:
            curr_path = str(curr_arr[0]) + "-" + str(curr_arr[1])

            # already proven true path
            if curr_path in visited_paths:
                continue
            else:
                visited_paths.add(curr_path)
                # parents are wanted courses
                parents = set()
                parents.add(curr_arr[0])

                # keep going for prerequisite courses
                next_course = curr_arr[1]
                result = dfs(parents, next_course)

                if result is False:
                    return False

        return True

