function fixPackages(packages: string): string {
     while (packages.includes('(')) {
        packages = packages.replace(/\(([^()]+)\)/g, (_, contenido) => {
            return contenido.split('').reverse().join('');
        });
    }
    return packages;
}