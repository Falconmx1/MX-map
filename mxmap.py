#!/usr/bin/env python3
import argparse
from mxmap.banner import show_banner
from mxmap.scanner import MXScanner

def main():
    show_banner()

    parser = argparse.ArgumentParser(description="MX-map - Herramienta de escaneo de puertos avanzada")
    parser.add_argument("-t", "--target", required=True, help="IP o dominio objetivo")
    parser.add_argument("-p", "--ports", default="1-1000", help="Rango de puertos (ej: 22,80 o 1-1000)")
    args = parser.parse_args()

    # Parsear puertos
    if "-" in args.ports:
        start, end = map(int, args.ports.split("-"))
        ports = range(start, end + 1)
    else:
        ports = [int(p) for p in args.ports.split(",")]

    scanner = MXScanner(args.target, ports)
    open_ports = scanner.run()

    print(f"\n\033[96m[+] Resultados para {args.target}: {open_ports}\033[0m")

if __name__ == "__main__":
    main()
