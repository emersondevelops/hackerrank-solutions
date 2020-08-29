using System;

namespace Day3IntroToConditionalStatements
{
    class Program
    {
        static void Main(string[] args)
        {
            int N = Convert.ToInt32(Console.ReadLine());

            if (N % 2 == 0)
            {
                if (N >= 2 && N <= 5)
                {
                    Console.WriteLine("Not Weird");
                }
                if (N >= 6 && N <= 20)
                {
                    Console.WriteLine("Weird");
                }
                if (N > 20)
                {
                    Console.WriteLine("Not Weird");
                }
            }
            else
            {
                Console.WriteLine("Weird");
            }
        }
    }
}
