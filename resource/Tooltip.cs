using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BG3TooltipExtract
{
    internal class Tooltip : IEquatable<Tooltip?>
    {
        public Tooltip(string tooltipName, string? type)
        {
            Name = tooltipName;
            Type = type;
        }

        public string Name { get; set; }
        public string? Type { get; set; }
        public string? DisplayName { get; set; }
        public string? DisplayNameCHS { get; set; }

        public override bool Equals(object? obj)
        {
            return Equals(obj as Tooltip);
        }

        public bool Equals(Tooltip? other)
        {
            return other is not null &&
                   Name == other.Name;
        }

        public override int GetHashCode()
        {
            return HashCode.Combine(Name);
        }


        public string ToENG()
        {
            return $"<LSTag Tooltip=\"{Name}\">{DisplayName}</LSTag>";
        }
        public string ToENG(bool haveType)
        {
            if (haveType)
            {
                return $"<LSTag Type=\"{Type}\" Tooltip=\"{Name}\">{DisplayName}</LSTag>";
            }
            else
                return ToENG();
        }
        public string ToCHS()
        {
            return $"<LSTag Tooltip=\"{Name}\">{DisplayNameCHS}</LSTag>";
        }
        public string ToCHS(bool haveType)
        {
            if (haveType)
            {
                return $"<LSTag Type=\"{Type}\" Tooltip=\"{Name}\">{DisplayNameCHS}</LSTag>";
            }
            else
                return ToCHS();
        }

        public static bool operator ==(Tooltip? left, Tooltip? right)
        {
            return EqualityComparer<Tooltip>.Default.Equals(left, right);
        }

        public static bool operator !=(Tooltip? left, Tooltip? right)
        {
            return !(left == right);
        }
    }
}
