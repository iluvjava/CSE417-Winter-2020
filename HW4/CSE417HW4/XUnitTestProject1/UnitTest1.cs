using System;
using Xunit;
using static System.Console;
using static HW4.KissMe;
using HW4;
using System.Collections.Generic;
using Xunit.Abstractions;
using System.Text;

namespace XUnitTestProject1
{
    public class UnitTest1
    {

        private readonly ITestOutputHelper output;

        public UnitTest1(ITestOutputHelper output)
        {
            this.output = output;
        }

        [Fact]
        public void Test1()
        {

        }

        [Fact]
        public void Test2()
        {
            WriteLine("This is the shit.");
        }


        [Fact]
        public void TestHW4()
        {
            HW4P4Print();
        }


        /// <summary>
        /// The result will get printed out to the console and 
        /// you should copy then and get the image elsewhere. 
        /// 
        /// The printed result will be formatted as json file for convenience. 
        /// </summary>
        public void HW4P4Print(
            int n = 1000,
            double p_start = 0.002,
            double p_end = 0.02,
            int N = 10)
        {
            double[] EdgeDensity = new double[N];
            StringBuilder sb = new StringBuilder();
            sb.AppendLine("[");

            for (double P = p_start, delta = (p_end - p_start) / N;
                P <= p_end;
                P += delta)
            {
                var G = new SimpleGraph(RandGraph(n, P));
                //output.WriteLine($"Ded Distribution with p = {P}; n = {n};");
                sb.AppendLine("{");
                sb.AppendLine($"\t\"p\":{P},");
                sb.AppendLine($"\t\"n\":{n},");
                foreach (KeyValuePair<int, int> kvp in G.GetDegStats())
                {
                    sb.AppendLine($"\t\"{kvp.Key}\": {kvp.Value},");
                }
                sb.Remove(sb.Length - 3, 2);
                sb.AppendLine("},");
            }
            sb.Remove(sb.Length - 3, 2);
            sb.AppendLine("]");
            output.WriteLine(sb.ToString());
        }

        [Fact]
        /// <summary>
        /// This is a static method that
        /// </summary>
        public void ColoringTest()
        {
            SimpleGraph thehypercube = HyperCubeConfigurations();
            int[] colors = thehypercube.GetColors();
            output.WriteLine("Verfies it by hand: ");
            for (int I = 0; I < colors.Length; I++)
            {
                output.WriteLine($"{I}:{colors[I]}");
            }
        }

        public static SimpleGraph HyperCubeConfigurations()
        {
            int[] arr1 = new int[] {0, 1, 3, 2, 2, 0, 1, 3, 7, 6, 5, 4};
            int[] arr2 = new int[] {1, 3, 2, 0, 7, 5, 5, 6, 6, 5, 4, 7};
            int n = 8;
            SimpleGraph res = SimpleGraph.MakeGraph(n, arr1, arr2);
            return res; 
        }


    }


}
