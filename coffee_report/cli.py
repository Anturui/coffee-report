import argparse
import sys
from typing import List
from .readers import read_csv_files
from .reports.registry import get_report, list_reports
from .formatters import format_table

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='Отчет о потреблении кофе',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Доступные отчеты:
  {', '.join(list_reports())}
        """
    )
    
    parser.add_argument(
        '--files',
        nargs='+',
        required=True,
        help='Пути к CSV файлам'
    )
    
    parser.add_argument(
        '--report',
        required=True,
        help='Название отчета для генерации'
    )
    
    return parser

def main(args: List[str] = None) -> int:
    parser = create_parser()
    parsed = parser.parse_args(args)
    
    try:
        data = read_csv_files(parsed.files)
        
        report = get_report(parsed.report, data)
        results = report.calculate()
        
        print(format_table(results, report.headers))
        
        return 0
        
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Неожиданная ошибка: {e}", file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())