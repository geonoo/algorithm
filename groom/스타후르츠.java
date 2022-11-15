package groom;

import java.io.*;

public class 스타후르츠 {
    

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int T = Integer.parseInt(input[1]);
        int C = Integer.parseInt(input[2]);
        int P = Integer.parseInt(input[3]);

        int a = (N / T) * C * P;
        System.out.println(a);
	}
}
