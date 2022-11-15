package groom;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.regex.Pattern;

class 단어개수세기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
        String[] arr = input.split(" ");
        int cnt = 0;
        for (String string : arr) {
            if (string.isEmpty()){
                continue;
            }
            boolean b = Pattern.matches("^[a-zA-Z]*$", string);
            if (b) cnt++;
        }
        System.out.println(cnt);
    }
}
