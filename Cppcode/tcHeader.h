/************************************************************************
 * This program is part of TimeCellScore, a set of time-cell scoring 
 * functions.
 * Copyright    (C) 2022    Upinder S. Bhalla and NCBS
 * It is made available under the terms of the
 * GNU Public License version 3 or later.
 * See the file COPYING.LIB for the full notice.
************************************************************************/

class AnalysisParams {
	public:
		AnalysisParams();
		unsigned int csOnsetFrame;
		unsigned int usOnsetFrame;
		unsigned int circPad;
		unsigned int circShuffleFrames;
		unsigned int binFrames;
		unsigned int numShuffle;
		double epsilon;
};

class TiAnalysisParams {
	public:
		TiAnalysisParams();
		double transientThresh;
		double tiPercentile;
		double fracTrialsFiredThresh;
		double frameDt;
};

struct CellScore {
	double meanScore; // pk of mean trace from Mau; r2b shuffled mean
	double baseScore;;	// Raw TI score, raw r2b ratio
	double percentileScore;	// Temporal info from Mau; r2b bootstrap
	bool sigMean;
	bool sigBootstrap;
	double fracTrialsFired;	// Hit Trial Ratio
	vector< double > meanTrace;
	unsigned int meanPkIdx;
};

// vector< CellScore > r2bScore(py::array_t<double> xs, const AnalysisParams& ap);
// vector< CellScore > tiScore( py::array_t<double> xs, const AnalysisParams& ap, const TiAnalysisParams& tip );
