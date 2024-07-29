{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = {
    nixpkgs,
    flake-utils,
    ...
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = nixpkgs.legacyPackages.${system};
    in {
      devShells.default = pkgs.mkShell {
        packages = with pkgs;
          [
            python312
            alejandra
          ]
          ++ (
            with python312Packages; [
              discordpy
              python-dotenv
              feedparser
              babel
              python-dateutil
            ]
          );
      };
    });
}
