//code from http://note.sonots.com/Comp/CompLang/cpp/getopt.html
/*
POSIX getopt for Windows

AT&T Public License

Code given out at the 1985 UNIFORUM conference in Dallas.
*/

#ifdef __cplusplus
extern "C" {
#endif

	extern int opterr;
	extern int optind;
	extern int optopt;
	extern char *optarg;
	extern int getopt(int argc, char **argv, char *opts);

#ifdef __cplusplus
}
#endif

