// This is the cBot I've used to download the data directly from cTrader backtesting

using System;
using cAlgo.API;
using cAlgo.API.Internals;
using System.IO;
using System.Text;
using System.Globalization;

namespace cAlgo.Robots
{
    [Robot(TimeZone = TimeZones.UTC, AccessRights = AccessRights.FullAccess)]
    public class SaveDataToCSV : Robot
    {
        private string _filePath;

        protected override void OnStart()
        {
            // Create a filename with the current system time
            var timestamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
            _filePath = $"/Users/pawelgach/Documents/Aarhus Uni/High Frequency Algorithmic Trading/data/BacktestData_{timestamp}.csv";

            // Write the header row with semicolon separator
            using (var writer = new StreamWriter(_filePath, false, Encoding.UTF8))
            {
                writer.WriteLine("Timestamp;Open;High;Low;Close;Volume");
            }
        }

        protected override void OnBar()
        {
            // Get the last completed bar index
            var lastBarIndex = Bars.ClosePrices.Count - 2;

            // Write the data for each bar to the CSV file with semicolon separator
            using (var writer = new StreamWriter(_filePath, true, Encoding.UTF8))
            {
                var line = string.Format(CultureInfo.InvariantCulture, "{0};{1:F4};{2:F4};{3:F4};{4:F4};{5}",
                    Bars.OpenTimes[lastBarIndex].ToString("yyyy-MM-dd HH:mm:ss"),
                    Bars.OpenPrices[lastBarIndex],
                    Bars.HighPrices[lastBarIndex],
                    Bars.LowPrices[lastBarIndex],
                    Bars.ClosePrices[lastBarIndex],
                    Bars.TickVolumes[lastBarIndex]);

                writer.WriteLine(line);
            }
        }

        protected override void OnStop()
        {
            // Optional: You can add any cleanup code here if needed
        }
    }
}