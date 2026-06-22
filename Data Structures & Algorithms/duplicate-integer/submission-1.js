class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const seen = [];
        for (const num of nums){
            if (seen.includes(num)){
                return true;
            }
            seen.push(num)
        }
        return false;
    }
}
