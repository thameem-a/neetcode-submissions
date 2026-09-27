class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        counter = 0 

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # check left 
                left_plot = i == 0 or flowerbed [i - 1] == 0
                # check right
                right_plot = i == len(flowerbed) -1 or flowerbed [i + 1] == 0
            
                if left_plot and right_plot:
                    flowerbed[i] = 1
                    counter += 1
        
        return counter >= n