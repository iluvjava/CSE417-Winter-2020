using NUnit.Framework;
using System.Collections.Generic;
using Problem5;
using static System.Console;
using System;
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
            Assert.Pass();
        }

        [Test]
        public void TestSimpleGraph()
        {

            IList<int>[] G = new List<int>[] 
            {
                new List<int>(){1, 2},
                new List<int>(){2, 0},
                new List<int>(){0, 1},
                new List<int>(){4},
                new List<int>(){3},
                new List<int>(),
            };
            var example = new SimpleGraphSearch(G);
            WriteLine(example);
        }

        [Test]
        public void RandomGraphConnectedComponents()
        {
            TestRandomGraphOnSize();
        }

        public void TestRandomGraphOnSize(int n = (int)1e4, double range = 1.5e-3)
        {
            int N = 30;
            double delta = range / N;
            double[] p = new double[N];
            for (int I = 0; I < N; I++)
            {
                p[I] = Math.Log(n)/n - range + (I + N/2) * delta;
            }

            for (int I = 0; I < p.Length; I++)
            {
                var G = KissMe.RandGraph(n, p[I]);
                var g = new SimpleGraphSearch(G);
                var res = g.ProduceStats();
                // string result = $"n= {n}; p = {p[I]}\n";
                // result += $"Total Components: {res[0]}\n";
                // result += $"Component Avg Size: {res[1]}\n";
                // result += $"Max Component Size: {res[2]}\n";
                // result += $"Min Component size: {res[3]}\n";
                // result += $"Component Size SD: {res[4]}\n\n";
                // Write(result);

                //0, 2, 3, 4
                WriteLine($"{n}, {p[I]}, {res[0]}, {res[2]}, {res[3]}, {res[4]}");
            }

        }
    }
}