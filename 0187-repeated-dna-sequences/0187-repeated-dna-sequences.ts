function findRepeatedDnaSequences(s: string): string[] {
    if(s.length < 10) return [];
    const set = new Set<string>();
    let left = 0, right = 10;
    const resultSet = new Set<string>();
    while(right <= s.length){
        let substr = s.substring(left, right);
        set.has(substr) ? resultSet.add(substr) : set.add(substr);
        left++, right++;
    }
    return [...resultSet];
};