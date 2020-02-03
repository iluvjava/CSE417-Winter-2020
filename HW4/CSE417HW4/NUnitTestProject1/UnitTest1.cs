using NUnit.Framework;
using HW4;
using System.Collections.Generic;
using static HW4.KissMe;
using static System.Console;

namespace Tests
{
    public class Tests
    {
        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void Test1()
        {
        }

        [Test]
        public void TestHW4()
        {
            HW4P4Print();
        }

        /// <summary>
        /// The result will get printed out to the console and 
        /// you should copy then and get the image elsewhere. 
        /// </summary>
        public static void HW4P4Print(
            int n = 1000,
            double p_start = 0.002,
            double p_end = 0.02,
            int N = 10)
        {
            double[] EdgeDensity = new double[N];
            for (double P = p_start, delta = (p_end - p_start) / N;
                P <= p_end;
                P += delta)
            {
                var G = new SimpleGraph(RandGraph(n, P));
                WriteLine($"Ded Distribution with p = {P}; n = {n};");
                foreach (KeyValuePair<int, int> kvp in G.GetDegStats())
                {
                    WriteLine($"Deg = {kvp.Key}, Frequency = {kvp.Value}");
                }
            }
        }
    }
}