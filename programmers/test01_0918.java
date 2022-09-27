package programmers;

import java.util.*;

public class test01_0918 {

    public static void main(String[] args) {
        String[] students = {"AAALLLAPAA", "AAAAAAAPPP", "ALAAAAPAAA"};
        //[3, 1, 2]

        // {"ALALLAAPAA", "ALLLAAAPAA", "APAPALLAAA"}
        // [1, 2, 3]
        System.out.println(Arrays.toString(solution(students)));
    }

    static public int[] solution(String[] students) {
        int[] answer = {};
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < students.length; i++) {
            int score = 10;
            int A = countChar(students[i], 'A');
            int L = countChar(students[i], 'L');
            int P = countChar(students[i], 'P');

            score += A;
            score = score - L/3;
            score -= P;
            if (P >= 3)
                score = 0;
            System.out.println(score);
            map.put(i, score);
        }
        List<Map.Entry<String, Integer>> entryList = new LinkedList<>(map.entrySet());
        entryList.sort(Map.Entry.comparingByValue());

        return answer;
    }

    public static int countChar(String str, char ch) {
        int count = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == ch) {
                count++;
            }        
        }         
        return count;    
    }
}
