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
            int n = (int)1e+4;
            {
                var G = KissMe.RandGraph(n, Math.Log(n) / n);
                var g = new SimpleGraphSearch(G);
                IDictionary<int, int> d = g.GetComponentSize();
                foreach (int k in d.Keys)
                {
                    WriteLine($"{k}: {d[k]}");
                }
            }

            {
                var G = KissMe.RandGraph(n, Math.Log(n)/n - 1e-4);
                var g = new SimpleGraphSearch(G);
                IDictionary<int, int> d = g.GetComponentSize();
                foreach (int k in d.Keys)
                {
                    WriteLine($"{k}: {d[k]}");
                }
            }
        }
    }
}