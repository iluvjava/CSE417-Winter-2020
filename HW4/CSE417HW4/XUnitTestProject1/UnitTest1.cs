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
        public void TestDegreeDistribution()
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
                var G = new ColoringGraph(RandGraph(n, P));
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
            ColoringGraph thehypercube = HyperCubeConfigurations();
            int[] colors = thehypercube.GetColors();
            output.WriteLine("Verfies it by hand: ");
            for (int I = 0; I < colors.Length; I++)
            {
                output.WriteLine($"{I}:{colors[I]}");
            }
        }

        [Fact]
        public void RandomGraphColoringTest()
        {
            output.WriteLine(RandomGraphColoringReport());
        }
        

        public static ColoringGraph HyperCubeConfigurations()
        {
            int[] aggregate = new int[] { 0, 1, 0, 2, 0, 4,
                                          3, 2, 3, 1, 3, 6,
                                          2, 7, 1, 5,
                                          7, 6, 6, 5, 5, 4, 4, 7};
            int[] arr1 = new int[12], arr2 = new int[12];
            for (int I = 0; I < arr1.Length; I++)
            {
                arr1[I] = aggregate[2*I];
                arr2[I] = aggregate[2 * I + 1];
            }
            int n = 8;
            ColoringGraph res = ColoringGraph.MakeGraph(n, arr1, arr2);
            return res; 
        }

        /// <summary>
        /// Generate a random graph and then use it to color it. 
        /// 
        /// This method investigate: 
        /// How much color is needed on average for a graph with 1000
        /// vertex, where p varies from 0.002 to 0.02 
        /// </summary>
        public static string RandomGraphColoringReport(
            int n = 1000,
            double p_start = 0.002,
            double p_end = 0.02,
            int N = 10, // Increment for edge density
            int samples = 100
            )
        {
            StringBuilder sb = new StringBuilder();
            sb.AppendLine("[");
            for (double p = p_start, delta = (p_end - p_start) / N; p <= p_end; p += delta)
            {
                sb.AppendLine("{");
                sb.AppendLine($"\"n\":{n},");
                sb.AppendLine($"\"p\":{p},");
                double avgColorUsed = Double.NaN;
                for (int I = 0; I < samples; I++)
                {
                    var aRandomGraph = new ColoringGraph(RandGraph(n, p));
                    avgColorUsed = Double.IsNaN(avgColorUsed) ? 0 : avgColorUsed;
                    avgColorUsed += aRandomGraph.ColorUsed();
                }
                avgColorUsed /= samples;
                sb.AppendLine($"\"AvgColor\": {avgColorUsed}");
                sb.AppendLine("},");
            }
            sb.AppendLine("]");

            return sb.ToString(); 
        }


    }


}
